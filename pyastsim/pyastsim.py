import itertools
import sys
import re
import argparse
import subprocess
import difflib

from ast import parse, NodeTransformer, copy_location, Name, FunctionDef, Expr, Str
import astunparse
import editdistance

class NormIdentifiers(NodeTransformer):
    def __init__(self):
        self.identifiers = {}
        super().__init__()

    def visit_Name(self, node):
        try:
            id = self.identifiers[node.id]
        except KeyError:
            id = f'id_{len(self.identifiers)}'
            self.identifiers[node.id] = id
        
        return  copy_location(Name(id=id), node)

class NormFunctions(NodeTransformer):
    def __init__(self, func=None):
        self.identifiers = {}
        self.func = func
        super().__init__()

    def visit_FunctionDef(self, node):
        if self.func and self.func != node.name:
            return None
    
        try:
            name = self.identifiers[node.name]
        except KeyError:
            name = f'function{len(self.identifiers):x}'
            self.identifiers[node.name] = name

        for i, arg in enumerate(node.args.args):
          arg.arg = f'arg{i}'

        new_func = FunctionDef(name=name, args=node.args, body=node.body, decorator_list=node.decorator_list)

        if isinstance(new_func.body[0], Expr) and isinstance(new_func.body[0].value, Str):
            del new_func.body[0]
        
        return  copy_location(new_func, node)

def get_normed_content(filename, func=None):
    if filename.endswith('.py'):
        with open(filename) as src:
            content = src.read()
            try:
                tree = parse(content)
            except SyntaxError:
                print(f"Syntax error in {filename}. Comparing non-normalized source.")
                return (filename, content)
        
            tree = NormFunctions(func=func).visit(tree)
            tree = NormIdentifiers().visit(tree)
        
            return (filename, astunparse.unparse(tree))

    if filename.endswith('.c') or filename.endswith('.cpp'):
        asm = subprocess.check_output(['gcc', '-S', '-o-', filename])
        return (filename, asm.decode('utf8'))

def get_pair_stats(pair):
    dld = editdistance.eval(pair[0][1], pair[1][1])
    avg_len = ( len(pair[0][1]) + len(pair[1][1]) ) / 2.0
    percent = 100.0 * (1 - (dld / avg_len))
    return((percent, dld, pair[0], pair[1]))

def main():
    ap = argparse.ArgumentParser(description='Check source files for similarity')
    ap.add_argument('--threshold', default=80, type=int, help="Similarity threshold. Values below this are not reported.")
    ap.add_argument('--show-diff', dest='show_diff', action='store_true', help="Show entire diff when reporting results.")
    ap.set_defaults(show_diff=False)
    ap.add_argument('--function', help="Specific function to compare (Python source only)")
    ap.add_argument('files', nargs='+', help="List of files to compare")

    args = ap.parse_args()

    submissions = [get_normed_content(f, args.function) for f in args.files]

    pairs = [get_pair_stats(pair) for pair in itertools.combinations(submissions, 2)]

    pairs.sort(key=lambda a: -a[0])

    return_code = 0

    for sim, dld, a, b in pairs:
        if sim > args.threshold:
            print(f"Detected pair similarity of {int(sim)}% with edit distance of {dld} for {a[0]} and {b[0]}\n")

            return_code = 1

            if args.show_diff:
                print('\n'.join(difflib.ndiff(a[1].splitlines(), b[1].splitlines())))

    exit(return_code)

if __name__ == '__main__':
  main()
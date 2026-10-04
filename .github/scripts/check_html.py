"""Fail if an HTML file has unclosed or mismatched tags."""
import sys
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "source", "track", "wbr"}


class Checker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.errors = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack or self.stack[-1][0] != tag:
            opened = f"<{self.stack[-1][0]}> from line {self.stack[-1][1]}" if self.stack else "nothing"
            self.errors.append(f"line {self.getpos()[0]}: </{tag}> closes {opened}")
            if any(t == tag for t, _ in self.stack):
                while self.stack and self.stack.pop()[0] != tag:
                    pass
        else:
            self.stack.pop()


failed = False
for path in sys.argv[1:]:
    c = Checker()
    c.feed(open(path, encoding="utf-8").read())
    c.close()
    c.errors += [f"<{t}> opened on line {n} is never closed" for t, n in c.stack]
    for e in c.errors:
        print(f"{path}: {e}")
    failed |= bool(c.errors)
    if not c.errors:
        print(f"{path}: OK")
sys.exit(1 if failed else 0)

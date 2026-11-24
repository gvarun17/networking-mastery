// Validate every ```mermaid block in the repo with the official Mermaid parser.
// Usage: (cd tools && npm ci) && node tools/validate_mermaid.mjs [files...]
import { JSDOM } from 'jsdom';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const dom = new JSDOM('<!doctype html><html><body></body></html>', { pretendToBeVisual: true });
globalThis.window = dom.window;
globalThis.document = dom.window.document;
Object.defineProperty(globalThis, 'navigator', { value: dom.window.navigator, configurable: true });
globalThis.Element = dom.window.Element;
globalThis.HTMLElement = dom.window.HTMLElement;
const { default: mermaid } = await import('mermaid');
mermaid.initialize({ startOnLoad: false });

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['node_modules', '.git'].includes(e.name)) continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, out);
    else if (p.endsWith('.md')) out.push(p);
  }
  return out;
}
const files = process.argv.length > 2 ? process.argv.slice(2) : walk(root);
let bad = 0, total = 0;
for (const f of files) {
  const txt = fs.readFileSync(f, 'utf8');
  const re = /```mermaid\n([\s\S]*?)```/g;
  let m;
  while ((m = re.exec(txt))) {
    total++;
    try { await mermaid.parse(m[1]); }
    catch (e) {
      bad++;
      const line = txt.slice(0, m.index).split('\n').length;
      console.log(`FAIL ${path.relative(root, f)}:${line}: ${String(e.message || e).split('\n').slice(0, 4).join(' | ')}`);
    }
  }
}
console.log(`mermaid blocks: ${total}, failures: ${bad}`);
process.exit(bad ? 1 : 0);

import type { Example } from '../types'

export default function CodeBlock({ example }: { example: Example }) {
  return (
    <div className="rounded-xl overflow-hidden border border-[#500000] my-3">
      <div className="bg-[#1a0a0a] text-[#e5c8c8] text-xs font-bold px-3 py-1.5 flex items-center justify-between">
        <span>script.py</span>
        <span className="text-[#7d8a80] font-normal">read-only</span>
      </div>
      <pre className="bg-[#0c0d0f] text-[#d9f2d9] text-sm p-3 overflow-x-auto">
        <code>{example.code}</code>
      </pre>
      <div className="bg-[#0a0a0a] text-xs font-bold text-[#7d8a80] px-3 py-1.5 border-t border-[#2a2c2f]">
        Output
      </div>
      <pre className="bg-[#050605] text-[#39ff14] text-sm p-3 overflow-x-auto whitespace-pre-wrap">
        <code>{example.output}</code>
      </pre>
      {example.note && (
        <p className="text-xs text-[#7d8a80] bg-[#101113] px-3 py-2 border-t border-[#2a2c2f]">{example.note}</p>
      )}
    </div>
  )
}

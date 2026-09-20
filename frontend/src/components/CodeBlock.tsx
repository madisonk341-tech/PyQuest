import type { Example } from '../types'

export default function CodeBlock({ example }: { example: Example }) {
  return (
    <div className="rounded-xl overflow-hidden border border-gray-200 my-3">
      <div className="bg-[#2b2b3d] text-gray-200 text-xs font-bold px-3 py-1.5 flex items-center justify-between">
        <span>script.py</span>
        <span className="text-gray-400 font-normal">read-only</span>
      </div>
      <pre className="bg-[#1e1e2e] text-[#e2e2f0] text-sm p-3 overflow-x-auto">
        <code>{example.code}</code>
      </pre>
      <div className="bg-[#111827] text-xs font-bold text-gray-400 px-3 py-1.5 border-t border-gray-700">
        Output
      </div>
      <pre className="bg-[#0b0f16] text-[#7ee787] text-sm p-3 overflow-x-auto whitespace-pre-wrap">
        <code>{example.output}</code>
      </pre>
      {example.note && (
        <p className="text-xs text-gray-500 bg-white px-3 py-2 border-t border-gray-100">{example.note}</p>
      )}
    </div>
  )
}

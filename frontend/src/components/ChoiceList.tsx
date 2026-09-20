export default function ChoiceList({
  choices,
  selected,
  correctIndex,
  revealed,
  onSelect,
}: {
  choices: string[]
  selected: number | null
  correctIndex?: number
  revealed?: boolean
  onSelect: (i: number) => void
}) {
  return (
    <div className="flex flex-col gap-2">
      {choices.map((c, i) => {
        let cls = 'border-[#2a2c2f] bg-[#101113] text-[#d9f2d9]'
        if (revealed) {
          if (i === correctIndex) cls = 'border-[#39ff14] bg-[#0f2408] text-[#39ff14]'
          else if (i === selected) cls = 'border-[#ff3b3b] bg-[#2a1010] text-[#ff8080]'
        } else if (i === selected) {
          cls = 'border-[#7a1f1f] bg-[#2a1414] text-[#eafff0]'
        }
        return (
          <button
            key={i}
            disabled={revealed}
            onClick={() => onSelect(i)}
            className={`text-left px-4 py-3 rounded-xl border-2 border-b-4 font-semibold text-sm transition whitespace-pre-line ${cls}`}
          >
            {c}
          </button>
        )
      })}
    </div>
  )
}

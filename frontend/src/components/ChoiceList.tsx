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
        let cls = 'border-gray-200 bg-white text-gray-800'
        if (revealed) {
          if (i === correctIndex) cls = 'border-[#58cc02] bg-[#d7ffb8] text-[#2b6b00]'
          else if (i === selected) cls = 'border-[#ff4b4b] bg-[#ffdfe0] text-[#b91c1c]'
        } else if (i === selected) {
          cls = 'border-[#1cb0f6] bg-[#ddf4ff] text-[#1899d6]'
        }
        return (
          <button
            key={i}
            disabled={revealed}
            onClick={() => onSelect(i)}
            className={`text-left px-4 py-3 rounded-xl border-2 border-b-4 font-semibold text-sm transition ${cls}`}
          >
            {c}
          </button>
        )
      })}
    </div>
  )
}

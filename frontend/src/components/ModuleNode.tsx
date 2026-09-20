import type { ModuleSummary } from '../types'

const COLORS = ['#58cc02', '#1cb0f6', '#ce82ff', '#ff9600', '#ff4b4b']

export default function ModuleNode({
  module,
  index,
  onClick,
}: {
  module: ModuleSummary
  index: number
  onClick: () => void
}) {
  const color = COLORS[index % COLORS.length]
  const pct = module.hasContent ? module.percentComplete : 0
  const locked = !module.hasContent
  const complete = pct >= 100

  const ringColor = locked ? '#e5e5e5' : color
  const bg =
    pct <= 0
      ? '#e5e5e5'
      : pct >= 100
        ? ringColor
        : `conic-gradient(${ringColor} ${pct * 3.6}deg, #e5e5e5 0deg)`

  return (
    <button
      onClick={onClick}
      className="relative flex flex-col items-center gap-1 group"
      style={{ width: 76 }}
      title={module.title}
    >
      <div
        className="rounded-full p-[5px] transition-transform group-active:scale-95"
        style={{ background: bg, width: 72, height: 72 }}
      >
        <div
          className="w-full h-full rounded-full flex items-center justify-center text-3xl shadow-inner"
          style={{ background: locked ? '#f2f2f2' : 'white', border: `2px solid ${locked ? '#e5e5e5' : color}` }}
        >
          {locked ? '🔒' : complete ? '✅' : module.icon}
        </div>
      </div>
      <span
        className="text-[11px] font-bold text-center leading-tight px-1 py-0.5 rounded-full"
        style={{ color: locked ? '#aaa' : '#4b4b4b' }}
      >
        {module.title.length > 22 ? `Mod ${module.id}` : module.title}
      </span>
    </button>
  )
}

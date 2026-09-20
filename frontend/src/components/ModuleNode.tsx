import type { ModuleSummary } from '../types'

const COLORS = ['#39ff14', '#500000', '#ffd200', '#1f8f0a', '#7a1f1f']

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

  const ringColor = locked ? '#2a2c2f' : color
  const bg =
    pct <= 0
      ? '#2a2c2f'
      : pct >= 100
        ? ringColor
        : `conic-gradient(${ringColor} ${pct * 3.6}deg, #2a2c2f 0deg)`

  return (
    <button
      onClick={onClick}
      className="relative flex flex-col items-center gap-1 group"
      style={{ width: 96 }}
      title={module.title}
    >
      <div
        className="rounded-full p-[5px] transition-transform group-active:scale-95"
        style={{ background: bg, width: 72, height: 72, boxShadow: locked ? 'none' : `0 0 12px ${color}55` }}
      >
        <div
          className="w-full h-full rounded-full flex items-center justify-center text-3xl"
          style={{ background: locked ? '#141517' : '#0c0d0f', border: `2px solid ${locked ? '#2a2c2f' : color}` }}
        >
          {locked ? '🔒' : complete ? '✅' : module.icon}
        </div>
      </div>
      <span
        className="text-[10px] font-bold text-center leading-tight"
        style={{ color: locked ? '#5a5f5a' : '#d9f2d9' }}
      >
        {module.title}
      </span>
    </button>
  )
}

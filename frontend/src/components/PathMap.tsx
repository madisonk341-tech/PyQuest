import type { ModuleSummary } from '../types'
import ModuleNode from './ModuleNode'

const ROW_HEIGHT = 118
const X_PATTERN = [0, -70, -95, -70, 0, 70, 95, 70]

export default function PathMap({
  modules,
  onSelect,
}: {
  modules: ModuleSummary[]
  onSelect: (m: ModuleSummary) => void
}) {
  const points = modules.map((m, i) => ({
    m,
    x: X_PATTERN[i % X_PATTERN.length],
    y: i * ROW_HEIGHT + 50,
  }))

  const height = points.length ? points[points.length - 1].y + 70 : 200

  return (
    <div className="relative mx-auto" style={{ width: 280, height }}>
      {/* footprint dots between consecutive nodes */}
      {points.slice(1).map((p, i) => {
        const prev = points[i]
        const steps = 5
        const dots = []
        for (let s = 1; s < steps; s++) {
          const t = s / steps
          const x = prev.x + (p.x - prev.x) * t
          const y = prev.y + (p.y - prev.y) * t
          dots.push(
            <span
              key={s}
              className="absolute rounded-full"
              style={{
                width: 6,
                height: 6,
                background: '#d8d8d8',
                left: `calc(50% + ${x}px)`,
                top: y,
                transform: 'translate(-50%, -50%)',
              }}
            />,
          )
        }
        return <div key={p.m.id}>{dots}</div>
      })}

      {points.map((p, i) => (
        <div
          key={p.m.id}
          className="absolute"
          style={{ left: `calc(50% + ${p.x}px)`, top: p.y, transform: 'translate(-50%, -50%)' }}
        >
          <ModuleNode module={p.m} index={i} onClick={() => onSelect(p.m)} />
        </div>
      ))}
    </div>
  )
}

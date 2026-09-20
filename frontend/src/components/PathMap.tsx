import type { ModuleSummary } from '../types'
import ModuleNode from './ModuleNode'

const ROW_HEIGHT = 220
const X_PATTERN = [0, -70, -95, -70, 0, 70, 95, 70]

// Deterministic pseudo-random bit so the "data trail" looks alive without
// flickering on every re-render (no Math.random()).
function bitAt(seed: number) {
  return (seed * 2654435761) % 7 < 3 ? '1' : '0'
}

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
    <div className="relative mx-auto" style={{ width: 300, height }}>
      {/* bit-sequence trail connecting consecutive nodes */}
      {points.slice(1).map((p, i) => {
        const prev = points[i]
        const active = p.m.hasContent || prev.m.hasContent
        // Only draw bits in the middle stretch of each segment — the ends
        // sit right where each node's own label is centered, so bits there
        // would overlap the module title text.
        const steps = 10
        const bits = []
        for (let s = 5; s <= 6; s++) {
          const t = s / steps
          const x = prev.x + (p.x - prev.x) * t
          const y = prev.y + (p.y - prev.y) * t
          bits.push(
            <span
              key={s}
              className="absolute font-mono select-none pointer-events-none"
              style={{
                fontSize: 11,
                fontWeight: 700,
                color: active ? '#39ff14' : '#3a3c3f',
                textShadow: active ? '0 0 4px rgba(57,255,20,0.6)' : 'none',
                left: `calc(50% + ${x}px)`,
                top: y,
                transform: 'translate(-50%, -50%)',
              }}
            >
              {bitAt(i * 13 + s * 5 + p.m.id.length)}
            </span>,
          )
        }
        return <div key={p.m.id}>{bits}</div>
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

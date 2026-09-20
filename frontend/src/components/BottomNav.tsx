import { NavLink } from 'react-router-dom'

const TABS = [
  { to: '/learning', label: 'Learning', icon: '🏠' },
  { to: '/practice', label: 'Practice', icon: '🎯' },
  { to: '/sandbox', label: 'Sandbox', icon: '💻' },
]

export default function BottomNav() {
  return (
    <nav className="fixed bottom-0 left-0 right-0 z-30 bg-[#0c0d0f] border-t border-[#2a2c2f] flex justify-around pb-[env(safe-area-inset-bottom)]">
      {TABS.map((t) => (
        <NavLink
          key={t.to}
          to={t.to}
          className={({ isActive }) =>
            `flex-1 flex flex-col items-center gap-0.5 py-2.5 text-xs font-bold transition ${
              isActive ? 'text-[#39ff14] pq-glow' : 'text-[#5a5f5a]'
            }`
          }
        >
          <span className="text-2xl leading-none">{t.icon}</span>
          {t.label}
        </NavLink>
      ))}
    </nav>
  )
}

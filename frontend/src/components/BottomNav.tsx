import { NavLink } from 'react-router-dom'

const TABS = [
  { to: '/learning', label: 'Learning', icon: '🏠' },
  { to: '/practice', label: 'Practice', icon: '🎯' },
  { to: '/sandbox', label: 'Sandbox', icon: '💻' },
]

export default function BottomNav() {
  return (
    <nav className="fixed bottom-0 left-0 right-0 z-30 bg-white border-t border-gray-200 flex justify-around pb-[env(safe-area-inset-bottom)]">
      {TABS.map((t) => (
        <NavLink
          key={t.to}
          to={t.to}
          className={({ isActive }) =>
            `flex-1 flex flex-col items-center gap-0.5 py-2.5 text-xs font-bold transition ${
              isActive ? 'text-[#58cc02]' : 'text-gray-400'
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

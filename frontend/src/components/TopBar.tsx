import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

export default function TopBar({ title }: { title: string }) {
  const { user, logout } = useAuth()
  const navigate = useNavigate()
  const [open, setOpen] = useState(false)

  return (
    <header className="sticky top-0 z-20 bg-[#0c0d0f] border-b border-[#2a2c2f] px-4 py-3 flex items-center justify-between">
      <h1 className="text-lg font-black text-[#39ff14] pq-glow tracking-wide">{title}</h1>
      <div className="relative">
        <button
          onClick={() => setOpen((o) => !o)}
          className="w-10 h-10 rounded-full bg-[#17181b] flex items-center justify-center text-xl border-2 border-[#500000]"
          aria-label="Profile"
        >
          {user?.avatar || '🙂'}
        </button>
        {open && (
          <div className="absolute right-0 mt-2 w-44 bg-[#101113] rounded-xl shadow-lg border border-[#2a2c2f] py-2 text-sm">
            <div className="px-3 pb-2 border-b border-[#2a2c2f]">
              <p className="font-bold text-[#eafff0] truncate">{user?.displayName}</p>
              <p className="text-[#7d8a80] text-xs">@{user?.username}</p>
            </div>
            <button
              onClick={async () => {
                await logout()
                navigate('/')
              }}
              className="w-full text-left px-3 py-2 text-[#ff3b3b] font-semibold hover:bg-[#17181b]"
            >
              Log out
            </button>
          </div>
        )}
      </div>
    </header>
  )
}

import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

export default function TopBar({ title }: { title: string }) {
  const { user, logout } = useAuth()
  const navigate = useNavigate()
  const [open, setOpen] = useState(false)

  return (
    <header className="sticky top-0 z-20 bg-white border-b border-gray-200 px-4 py-3 flex items-center justify-between">
      <h1 className="text-lg font-black text-gray-800">{title}</h1>
      <div className="relative">
        <button
          onClick={() => setOpen((o) => !o)}
          className="w-10 h-10 rounded-full bg-gray-100 flex items-center justify-center text-xl border-2 border-gray-200"
          aria-label="Profile"
        >
          {user?.avatar || '🙂'}
        </button>
        {open && (
          <div className="absolute right-0 mt-2 w-44 bg-white rounded-xl shadow-lg border border-gray-100 py-2 text-sm">
            <div className="px-3 pb-2 border-b border-gray-100">
              <p className="font-bold text-gray-800 truncate">{user?.displayName}</p>
              <p className="text-gray-400 text-xs">@{user?.username}</p>
            </div>
            <button
              onClick={async () => {
                await logout()
                navigate('/')
              }}
              className="w-full text-left px-3 py-2 text-[#ff4b4b] font-semibold hover:bg-gray-50"
            >
              Log out
            </button>
          </div>
        )}
      </div>
    </header>
  )
}

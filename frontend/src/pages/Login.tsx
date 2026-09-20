import { useState, type FormEvent } from 'react'
import { useNavigate } from 'react-router-dom'
import { ApiError, useAuth } from '../context/AuthContext'

const FLOATERS = ['01001', '{ }', '==', '10110', 'import', '11001', 'def f():', '01100', '#!/usr/bin', '10011', 'while True:', '00101']

export default function Login() {
  const { login, register } = useAuth()
  const navigate = useNavigate()
  const [mode, setMode] = useState<'login' | 'register'>('login')
  const [username, setUsername] = useState('')
  const [displayName, setDisplayName] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [error, setError] = useState('')
  const [busy, setBusy] = useState(false)

  async function onSubmit(e: FormEvent) {
    e.preventDefault()
    setError('')

    if (mode === 'register' && password !== confirmPassword) {
      setError('Passwords do not match.')
      return
    }

    setBusy(true)
    try {
      if (mode === 'login') {
        await login(username, password)
      } else {
        await register(username, password, displayName || username)
      }
      navigate('/learning')
    } catch (err) {
      setError(err instanceof ApiError ? err.message : 'Something went wrong.')
    } finally {
      setBusy(false)
    }
  }

  return (
    <div className="relative min-h-screen overflow-hidden flex items-center justify-center bg-[#08090a] px-4">
      <div
        aria-hidden
        className="pointer-events-none absolute inset-0"
        style={{
          background:
            'radial-gradient(ellipse at 50% 0%, rgba(80,0,0,0.35) 0%, transparent 55%), radial-gradient(ellipse at 50% 100%, rgba(57,255,20,0.08) 0%, transparent 60%)',
        }}
      />
      <div aria-hidden className="pointer-events-none absolute inset-0 overflow-hidden">
        {FLOATERS.map((f, i) => (
          <span
            key={i}
            className="pq-float pq-flicker absolute font-mono font-bold select-none"
            style={{
              left: `${(i * 37) % 100}%`,
              top: `${(i * 53) % 100}%`,
              fontSize: `${14 + (i % 4) * 8}px`,
              color: i % 3 === 0 ? 'rgba(122,31,31,0.55)' : 'rgba(57,255,20,0.35)',
              animationDelay: `${i * 0.4}s`,
              animationDuration: `${5 + (i % 3)}s`,
            }}
          >
            {f}
          </span>
        ))}
      </div>

      <div className="relative z-10 w-full max-w-sm">
        <div className="text-center mb-6">
          <div className="text-6xl mb-2">🐍</div>
          <h1 className="text-4xl font-black text-[#39ff14] pq-glow tracking-tight">
            &gt;_ PyQuest
          </h1>
        </div>

        <form
          onSubmit={onSubmit}
          className="bg-[#101113] border border-[#500000] rounded-2xl shadow-[0_0_30px_rgba(57,255,20,0.08)] p-6 flex flex-col gap-3"
        >
          <div className="flex rounded-xl bg-[#0c0d0f] p-1 mb-1 border border-[#2a2c2f]">
            <button
              type="button"
              onClick={() => setMode('login')}
              className={`flex-1 py-2 rounded-lg font-bold text-sm transition ${mode === 'login' ? 'bg-[#500000] text-[#eafff0]' : 'text-[#7d8a80]'}`}
            >
              Log In
            </button>
            <button
              type="button"
              onClick={() => setMode('register')}
              className={`flex-1 py-2 rounded-lg font-bold text-sm transition ${mode === 'register' ? 'bg-[#500000] text-[#eafff0]' : 'text-[#7d8a80]'}`}
            >
              Sign Up
            </button>
          </div>

          <label className="text-left text-xs font-bold text-[#7d8a80] uppercase tracking-wide">
            Username
            <input
              required
              minLength={3}
              maxLength={20}
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="mt-1 w-full border-2 border-[#2a2c2f] bg-[#0c0d0f] text-[#eafff0] rounded-xl px-3 py-2 text-base font-medium focus:outline-none focus:border-[#39ff14]"
              placeholder="pythonista22"
            />
          </label>

          {mode === 'register' && (
            <label className="text-left text-xs font-bold text-[#7d8a80] uppercase tracking-wide">
              Display name
              <input
                value={displayName}
                onChange={(e) => setDisplayName(e.target.value)}
                className="mt-1 w-full border-2 border-[#2a2c2f] bg-[#0c0d0f] text-[#eafff0] rounded-xl px-3 py-2 text-base font-medium focus:outline-none focus:border-[#39ff14]"
                placeholder="What should we call you?"
              />
            </label>
          )}

          <label className="text-left text-xs font-bold text-[#7d8a80] uppercase tracking-wide">
            Password
            <input
              required
              minLength={6}
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="mt-1 w-full border-2 border-[#2a2c2f] bg-[#0c0d0f] text-[#eafff0] rounded-xl px-3 py-2 text-base font-medium focus:outline-none focus:border-[#39ff14]"
              placeholder="••••••••"
            />
          </label>

          {mode === 'register' && (
            <label className="text-left text-xs font-bold text-[#7d8a80] uppercase tracking-wide">
              Confirm password
              <input
                required
                minLength={6}
                type="password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                className="mt-1 w-full border-2 border-[#2a2c2f] bg-[#0c0d0f] text-[#eafff0] rounded-xl px-3 py-2 text-base font-medium focus:outline-none focus:border-[#39ff14]"
                placeholder="••••••••"
              />
            </label>
          )}

          {error && <p className="text-[#ff3b3b] text-sm font-semibold">{error}</p>}

          <button type="submit" disabled={busy} className="pq-btn pq-btn-green mt-2 py-3 text-sm">
            {busy ? 'One sec…' : mode === 'login' ? 'Log In' : 'Create Account'}
          </button>
        </form>
      </div>
    </div>
  )
}

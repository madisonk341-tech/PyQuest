import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { api } from '../api/client'
import BottomNav from '../components/BottomNav'
import PathMap from '../components/PathMap'
import TopBar from '../components/TopBar'
import type { ModuleSummary } from '../types'

export default function Learning() {
  const [modules, setModules] = useState<ModuleSummary[] | null>(null)
  const navigate = useNavigate()

  useEffect(() => {
    api.get<{ modules: ModuleSummary[] }>('/modules').then((r) => setModules(r.modules))
  }, [])

  const overall = modules
    ? Math.round(
        modules.filter((m) => m.hasContent).reduce((s, m) => s + m.percentComplete, 0) /
          Math.max(1, modules.filter((m) => m.hasContent).length),
      )
    : 0

  return (
    <div className="min-h-screen pb-24 bg-[#f7f7f7]">
      <TopBar title="Learning" />

      <div className="px-4 pt-4">
        <div className="bg-white rounded-2xl border border-gray-200 p-3 flex items-center gap-3 max-w-sm mx-auto mb-4">
          <span className="text-2xl">🔥</span>
          <div className="flex-1">
            <p className="text-xs font-bold text-gray-400 uppercase">Overall progress</p>
            <div className="w-full bg-gray-100 rounded-full h-2 mt-1">
              <div
                className="h-2 rounded-full bg-[#58cc02] transition-all"
                style={{ width: `${overall}%` }}
              />
            </div>
          </div>
          <span className="font-black text-[#58cc02]">{overall}%</span>
        </div>
      </div>

      {!modules && <p className="text-center text-gray-400 mt-10">Loading modules…</p>}

      {modules && (
        <div className="pt-2">
          <PathMap modules={modules} onSelect={(m) => navigate(`/learning/${m.id}`)} />
        </div>
      )}

      <BottomNav />
    </div>
  )
}

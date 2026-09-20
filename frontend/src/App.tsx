import type { ReactNode } from 'react'
import { Navigate, Route, Routes } from 'react-router-dom'
import { AuthProvider, useAuth } from './context/AuthContext'
import Learning from './pages/Learning'
import Login from './pages/Login'
import ModuleDetail from './pages/ModuleDetail'
import Practice from './pages/Practice'
import Sandbox from './pages/Sandbox'

function RequireAuth({ children }: { children: ReactNode }) {
  const { user, loading } = useAuth()
  if (loading) {
    return <div className="min-h-screen flex items-center justify-center text-gray-400">Loading…</div>
  }
  if (!user) return <Navigate to="/" replace />
  return <>{children}</>
}

function RedirectIfAuthed({ children }: { children: ReactNode }) {
  const { user, loading } = useAuth()
  if (loading) {
    return <div className="min-h-screen flex items-center justify-center text-gray-400">Loading…</div>
  }
  if (user) return <Navigate to="/learning" replace />
  return <>{children}</>
}

export default function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route
          path="/"
          element={
            <RedirectIfAuthed>
              <Login />
            </RedirectIfAuthed>
          }
        />
        <Route
          path="/learning"
          element={
            <RequireAuth>
              <Learning />
            </RequireAuth>
          }
        />
        <Route
          path="/learning/:moduleId"
          element={
            <RequireAuth>
              <ModuleDetail />
            </RequireAuth>
          }
        />
        <Route
          path="/practice"
          element={
            <RequireAuth>
              <Practice />
            </RequireAuth>
          }
        />
        <Route
          path="/sandbox"
          element={
            <RequireAuth>
              <Sandbox />
            </RequireAuth>
          }
        />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </AuthProvider>
  )
}

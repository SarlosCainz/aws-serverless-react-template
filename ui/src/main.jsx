import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom';
import App, {AppProvider, UserProvider} from './App'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
      <BrowserRouter>
          <AppProvider>
              <UserProvider>
                  <App />
              </UserProvider>
          </AppProvider>
      </BrowserRouter>
  </React.StrictMode>,
)

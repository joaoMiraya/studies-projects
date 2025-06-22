
import '../stylesheets/index.css'
import App from '../App.tsx'
import { createBrowserRouter, RouterProvider } from 'react-router';
import ReactDOM from "react-dom/client";
import { Home } from '../pages/Home.tsx';
import { Admin } from '../pages/Admin.tsx';
import { History } from '../pages/History.tsx';

const router = createBrowserRouter([
  {
    path: "/",
    Component: App,
    children: [
      { index: true, Component: Home },
      { path: "admin", Component: Admin },
      { path: "history", Component: History },
    ],
  },
  {
    path: "*",
    Component: () =>
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-2xl font-bold">Página não encontrada</h1>
    </div>,
  }
  
]);


const root = document.getElementById("root");
if (!root) {
  throw new Error("Root element not found");
}

ReactDOM.createRoot(root).render(
  <RouterProvider router={router} />
);


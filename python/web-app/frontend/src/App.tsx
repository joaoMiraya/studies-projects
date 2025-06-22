import { Outlet } from "react-router"
import { Header } from "./components/partials/Header"
import { Footer } from "./components/partials/Footer"
import { CartProvider } from "../context/useCartContext"


function App() {

  return (
    <>
      <Header />
      <CartProvider>
        <Outlet />
      </CartProvider>
      <Footer />
    </>
  )
}

export default App

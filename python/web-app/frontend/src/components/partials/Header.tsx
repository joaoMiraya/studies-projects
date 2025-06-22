import { Link } from "react-router"


export const Header = () => {

    return (
        <header>
            <nav className="bg-gray-800 p-4">
                <div className="container mx-auto flex justify-between items-center">
                    <div className="text-white text-lg font-bold">Big Bom</div>
                    <ul className="flex space-x-4">
                        <li><Link to="/admin" className="text-white hover:text-gray-400">Admin</Link></li>
                        <li><Link to="/" className="text-white hover:text-gray-400">Comprar</Link></li>
                        <li><Link to="/history" className="text-white hover:text-gray-400">Histórico de pedidos</Link></li>
                    </ul>
                </div>
            </nav>
        </header>
    )
}
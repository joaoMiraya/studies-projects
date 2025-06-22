import { Link } from "react-router";


export const Footer = () => {
const currentYear = new Date().getFullYear();

    return (
        <header>
            <nav className="bg-gray-800 p-4">
                <div className="container mx-auto flex justify-between items-center">
                    <div className="text-white text-lg font-bold">Big Bom</div>
                    <ul className="flex space-x-4">
                        <li><Link to="/" className="text-white hover:text-gray-400">Comprar</Link></li>
                    </ul>
                    <div className="text-white text-sm">&copy; {currentYear} Big Bom. Todos os direitos reservados.</div>
                </div>
            </nav>
        </header>
    )
}
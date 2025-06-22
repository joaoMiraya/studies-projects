import { useCart } from "../../../context/useCartContext";
import { createOrder, type Order } from "../../services/api";
import { maskCurrencyBRL } from "../../services/utils";

export const Cart = () => {
    const { items: cartItems, totalPrice, clearCart } = useCart();


    const handleClearCart = () => {
        clearCart();
    };

    const handleCreateOrder = async () => {
        try {
            const orderItems: Order[] = cartItems.map((item) => ({
                product_id: item.id,
                quantity: item.quantity,
            }));
            await createOrder(orderItems);
            handleClearCart();
        } catch (error) {
            console.error('Error creating order:', error);
        }
    };
    
    return (
    
        <div className="mb-8 bg-white p-4 rounded-md shadow-inner flex-grow-1 border-1 border-gray-300">
            <h2 className="text-xl font-bold mb-4">Carrinho de compras</h2>
            {cartItems.length > 0 ? (
                <>
                    <ul className="space-y-2">
                        {cartItems.map((cartItem) => (
                            <li key={cartItem.id} className="flex justify-between items-center p-2 border-b">
                                <div>
                                    <span className="font-medium">{cartItem.name}</span>
                                    <span className="text-sm text-gray-600 ml-2">
                                        x{cartItem.quantity}
                                    </span>
                                </div>
                                <span className="text-green-700 font-semibold">
                                    {maskCurrencyBRL(String(cartItem.price * cartItem.quantity))}
                                </span>
                            </li>
                        ))}
                    </ul>
                    <div className="flex justify-end mt-4">
                        <button className="text-gray-400 underline cursor-pointer text-end" onClick={() => handleClearCart()}>Limpar</button>
                    </div>
                    <div className="mt-4 pt-4">
                        <div className="flex justify-between items-center font-bold text-lg">
                            <span>Total:</span>
                            <span className="text-green-700">
                                {maskCurrencyBRL(String(totalPrice))}
                            </span>
                        </div>
                        <button onClick={() => handleCreateOrder()}
                            className="bg-blue-500 p-2 rounded-sm w-full mt-6 cursor-pointer text-white hover:bg-blue-400 transition-colors duration-300"
                        >
                            Comprar
                        </button>
                    </div>
                </>
            ) : 
                <div className="text-gray-500 text-center">
                    Seu carrinho está vazio.
                </div>
            }
        </div>
    );
}
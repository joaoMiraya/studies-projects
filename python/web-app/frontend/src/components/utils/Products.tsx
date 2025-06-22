import { useEffect, useState } from "react";
import { getItems, type Item } from "../../services/api";
import { useCart, type Product } from "../../../context/useCartContext";
import { maskCurrencyBRL } from "../../services/utils";

export const Products = () => {
    const [items, setItems] = useState<Item[]>([]);
    const { addItem, removeItem, updateQuantity, items: cartItems} = useCart();

    const handleFetch = async () => {
        const items = await getItems();
        if (items) {
            setItems(items);
        }
    };

    useEffect(() => {
        handleFetch();
    }, []);

    const handleAddToCart = (item: Item) => {
        const product: Product = {
            id: item.id,
            name: item.name,
            price: item.price,
        };
        
        addItem(product, 1);
    };

    const handleRemoveOneFromCart = (itemId: number) => {
        const cartItem = cartItems.find(item => item.id === itemId);
        if (cartItem) {
            if (cartItem.quantity > 1) {
                updateQuantity(itemId, cartItem.quantity - 1);
            } else {
                removeItem(itemId);
            }
        }
    };

    const handleRemoveAllFromCart = (itemId: number) => {
        removeItem(itemId);
    };

    const getItemQuantityInCart = (itemId: number): number => {
        const cartItem = cartItems.find(item => item.id === itemId);
        return cartItem ? cartItem.quantity : 0;
    };

    return (
        <>
            <ul className="space-y-2 max-h-[30rem] overflow-y-auto">
                {items.map((item) => {
                    const quantityInCart = getItemQuantityInCart(item.id);
                    
                    return (
                        <li key={item.id} className="border min-w-[18rem] border-gray-300 rounded-md bg-white shadow-sm flex flex-col items-start gap-4 p-4">
                            <div className="flex flex-col">
                                <span className="font-semibold">{item.name}</span>
                                {quantityInCart > 0 && (
                                    <span className="text-sm text-blue-600">
                                        {quantityInCart} no carrinho
                                    </span>
                                )}
                            </div>
                            
                            <div className="flex items-center justify-between w-full gap-2">
                                <span className="text-green-700 font-semibold">
                                    {maskCurrencyBRL(String(item.price))}
                                </span>
                                
                                {quantityInCart > 0 ? (
                                    <div className="flex items-center justify-between w-full gap-2">
                                        <button 
                                            onClick={() => handleRemoveOneFromCart(item.id)}
                                            className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded-md text-sm transition-colors cursor-pointer"
                                        >
                                            -
                                        </button>
                                        
                                        <span className="mx-2 font-semibold">
                                            {quantityInCart}
                                        </span>
                                        
                                        <button 
                                            onClick={() => handleAddToCart(item)}
                                            className="bg-green-500 hover:bg-green-600 text-white px-3 py-1 rounded-md text-sm transition-colors cursor-pointer"
                                        >
                                            +
                                        </button>
                                        
                                        <button 
                                            onClick={() => handleRemoveAllFromCart(item.id)}
                                            className="text-gray-400 px-3 py-1 rounded-md text-sm ml-2 underline cursor-pointer"
                                        >
                                            Remover Todos
                                        </button>
                                    </div>
                                ) : (
                                    <button 
                                        onClick={() => handleAddToCart(item)} 
                                        className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-md transition-colors cursor-pointer"
                                    >
                                        Adicionar
                                    </button>
                                )}
                            </div>
                        </li>
                    );
                })}
            </ul>
        </>
    );
}
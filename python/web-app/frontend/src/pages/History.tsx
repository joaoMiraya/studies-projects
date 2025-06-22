import { useEffect, useState } from "react";
import { getOrders, type HistoryOrder } from "../services/api";
import { formatDateTime } from "../services/utils";

export const History = () => {
    const [orders, setOrders] = useState<HistoryOrder[]>([]);

    useEffect(() => {
        const fetchOrders = async () => {
            try {
                const fetchedOrders = await getOrders();
                setOrders(fetchedOrders);
            } catch (error) {
                console.error('Error fetching orders:', error);
            }
        }
        fetchOrders();
    }, []);
    
    return (
        <>
            <div className="flex flex-col items-start justify-center min-h-screen bg-gray-100">
                <h1 className="text-2xl my-6 ml-12 font-bold self-start">Histórico de Compras</h1>
                <div className="w-full max-w-4xl px-12">
                    {orders.length > 0 ? (
                        <ul className="space-y-4">
                            {orders.map((order, i) => (
                                <li key={i} className="border border-gray-300 rounded-md bg-white shadow-sm p-4">
                                    <h2 className="text-lg font-semibold mb-2">Pedido #{i}</h2>
                                    <p className="text-gray-600 mb-2">{formatDateTime(order.order_date)}</p>
                                    <ul className="space-y-2">
                                        {order.items.map((item, i) => (
                                            <li key={i} className="flex justify-between">
                                                <p>{item.product.name}</p>
                                                {`${item.quantity} x R$ ${item.price_at_order}`}
                                            </li>
                                        ))}
                                    </ul>
                                    <div className="mt-4 font-bold text-lg">
                                        Total: R$ {order.total.toFixed(2)}
                                    </div>  
                                </li>
                            ))}
                        </ul>
                    ) : (
                        <p className="text-gray-600">Nenhum pedido encontrado.</p>
                    )}
                </div>
            </div>
        </>
    );
}
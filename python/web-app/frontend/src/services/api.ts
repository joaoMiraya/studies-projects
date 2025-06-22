import axios from 'axios';

export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export interface Item {
    id: number;
    name: string;
    category: string;
    price: number;
};


export interface PublicItem {
    name: string;
    category: string;
    price: number  | string;
};

export interface Order {
    product_id: number;
    quantity: number;
};
export interface OrderItem {
    price_at_order: number;
    product: Item;
    quantity: number;
    subtotal: number;
};
export interface HistoryOrder {
    items: OrderItem[];
    order_date: string;
    total: number;
};

export const getItems = async (): Promise<Item[]> => {
    try {
        const response = await axios.get(`${API_BASE_URL}/products/`);
        return response.data;
    } catch (error) {
        console.error('Error fetching items:', error);
        throw error;
    }
};

export const createNewItem = async (item: PublicItem): Promise<Item> => {
    try {
        const response = await axios.post(`${API_BASE_URL}/product/`, item);
        return response.data;
    } catch (error) {
        console.error('Error creating item:', error);
        throw error;
    }
}

export const createOrder = async (order: Order[]) => {
    try {
        const payload = {
            items: order
        };
        const response = await axios.post(`${API_BASE_URL}/order/`, payload);
        return response.data;
    } catch (error) {
        console.error('Error creating item:', error);
        throw error;
    }
}

export const getOrders = async (): Promise<HistoryOrder[]> => {
    try {
        const response = await axios.get(`${API_BASE_URL}/orders/`);
        return response.data;
    } catch (error) {
        console.error('Error fetching items:', error);
        throw error;
    }
};
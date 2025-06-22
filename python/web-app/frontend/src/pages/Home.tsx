import { Cart } from "../components/utils/Cart";
import { Products } from "../components/utils/Products";

export const Home = () => {



    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
            <h1 className="text-2xl my-6 ml-12 font-bold self-start">Produtos</h1>
            <div className="w-full max-w-4xl flex gap-[2rem] items-start justify-center flex-wrap px-12">
                <Products />
                <Cart />
            </div>
        </div>
    );
};
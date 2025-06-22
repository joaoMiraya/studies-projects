import { useState, type FormEvent } from "react";
import { createNewItem, type PublicItem } from "../../services/api";
import { parseBRLToNumber } from "../../services/utils";


export const Create = () => {
    const [product, setProduct] = useState<PublicItem>({
        name: '',
        price: '',
        category: '',
    });

    const handleCreateProduct = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        if (!product.name || !product.category || parseBRLToNumber((String(product.price))) <= 0) {
            alert("Por favor, preencha todos os campos corretamente.");
            return;
        }
        const item: PublicItem = {
            ...product
        };
        try {
            await createNewItem(item);
            alert(`Produto ${product.name} adicionado com sucesso!`);
        } catch (error) {
            console.error("Erro ao criar produto:", error);
            alert("Erro ao criar produto. Tente novamente.");
            return;
        }
    };

    return (
        <>
            <div>
                <form onSubmit={(e) => handleCreateProduct(e)}
                 className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
                     <h2 className="mb-4">Adicione um novo produto no estoque!</h2>
                    <input
                        type="text"
                        placeholder="Nome do Produto"
                        className="mb-4 p-2 border border-gray-300 rounded"
                        value={product.name}
                        onChange={(e) => setProduct({ ...product, name: e.target.value })}
                    />
                    <input
                        type="text"
                        placeholder="Categoria do Produto"
                        className="mb-4 p-2 border border-gray-300 rounded"
                        value={product.category}
                        onChange={(e) => setProduct({ ...product, category: e.target.value })}
                    />
                    <input
                        type="number"
                        placeholder="Preço do Produto"
                        className="mb-4 p-2 border border-gray-300 rounded"
                        value={product.price}
                        onChange={(e) => setProduct({ ...product, price: e.target.value})}
                    />
                    <button
                        type="submit"
                        className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
                    >
                        Adicionar Produto
                    </button>
                </form>
            </div>
        </>
    )
}
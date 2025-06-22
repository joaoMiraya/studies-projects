export const parseBRLToNumber = (formatted: string): number => {
  const cleaned = formatted.replace(/\s|R\$|\./g, '').replace(',', '.');

  const result = parseFloat(cleaned);

  if (isNaN(result)) {
    throw new Error('Valor formatado inválido');
  }

  return result;
}

export const maskCurrencyBRL = (value: string | number): string => {
  let numeric: number;
  if (typeof value === 'number') {
    numeric = value;
  } else {
    const cleaned = value.replace(/[^\d,.-]/g, '').replace(',', '.');
    numeric = parseFloat(cleaned) || 0;
  }

  return numeric.toLocaleString('pt-BR', {
    style: 'currency',
    currency: 'BRL'
  });
};

export const formatDateTime = (isoString: string): string => {
  const date = new Date(isoString);

  const pad = (num: number): string => num.toString().padStart(2, '0');

  const day = pad(date.getDate());
  const month = pad(date.getMonth() + 1);
  const year = date.getFullYear();

  const hours = pad(date.getHours());
  const minutes = pad(date.getMinutes());

  return `${day}-${month}-${year} - ${hours}:${minutes}`;
};

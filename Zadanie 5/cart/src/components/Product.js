import React from 'react'

export default function Product(props) {
    const{product, onAdd}=props;
  return (
    <div>
        <img className='small' scr={product.image} alt={product.name}></img>
        <h3>{product.name}</h3>
        <div>{product.price} zł</div>
        <div>
            <button onClick ={() => onAdd(product)}>Kup</button>
        </div>

    </div>
  );
}

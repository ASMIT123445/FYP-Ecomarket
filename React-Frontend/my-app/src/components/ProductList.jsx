import React, { useEffect, useState } from "react";
import axios from "axios";

function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // This is where the Axios example goes
    axios.get("http://127.0.0.1:8000/api/products/")
      .then(res => setProducts(res.data)) // save to state
      .catch(err => console.error(err));
  }, []); // empty dependency = run once when component mounts

  return (
    <div>
      <h2>Product List</h2>
      <ul>
        {products.map(p => (
          <li key={p.id}>{p.name} - Rs.{p.price}</li>
        ))}
      </ul>
    </div>
  );
}

export default ProductList;
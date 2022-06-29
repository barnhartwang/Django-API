import axios from 'axios';
import {useState, useEffect} from 'react'
import './App.css';

function App() {
  const [list, setList] = useState([]);
  useEffect(() => 
    getData()
    ,[]);
  const getData = () =>{
    axios.get('http://127.0.0.1:8000/api/')
    .then (response => {
      console.log(response);
      setList(response.data);
  })
    .catch ( error => console.log(error));
  }
  return (
    <div className="App">
      {list.map(item =>(
           
        <div key={item.id}>
          <h1>{item.title}</h1>
          <p>{item.body}</p>
        </div>

      ))}
    </div>
  );
}

export default App;

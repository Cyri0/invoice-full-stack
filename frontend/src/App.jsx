import React, {useState, useEffect} from 'react'
import Invoice from './components/Invoice'

const App = () => {
  const [invoices, setInvoices] = useState([])

  useEffect(()=>{

    fetch('/invoices')
    .then(res => res.json())
    .then(data => {
      setInvoices(data)
    })
    
  },[])

  return (
    <div>

      {invoices.map(invoice => <Invoice data = {invoice} />)}

    </div>
  )
}

export default App

// rafce
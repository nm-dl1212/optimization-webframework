import React, {useState, useEffect} from 'react'
import axios from 'axios'

interface Task {
  id: number;
  title: string;
}

const DjangoApiFetch = () => {

  const [tasks, setTasks] = useState<Task[]>([])

  useEffect(()=>{
    axios.get('http://127.0.0.1:8000/api/tasks/', {
      headers:{'Authorization': 'Token 5eacc696679008eb40c1758a665c8d369c57174e'}
    })
    .then(res => {setTasks(res.data)})
  }, [])

  return (
    <div>
      <ul>
        {
          tasks.map(task => <li key={task.id}>{task.title}</li>)
        }
      </ul>
      test
    </div>
  )
}

export default DjangoApiFetch
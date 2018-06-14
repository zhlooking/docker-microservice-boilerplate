import React from 'react'

export default props => (
  <div>
    {
      props.users.map(user => (
        <h4
          key={user.id}
          className="card card-body bg-light"
        >{user.username}
        </h4>
      ))
    }
  </div>
)

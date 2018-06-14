/* REACT_APP_USERS_SERVICE_URL */
import React from 'react'
import axios from 'axios'
import PropTypes from 'prop-types'
import { observer, inject } from 'mobx-react'
import UserStore from '../store/user-store'
import UserList from './user_list'
import '../css/users.scss'

@inject('userStore')
@observer
export default class Users extends React.Component {
  static propTypes = {
    userStore: PropTypes.instanceOf(UserStore).isRequired,
  }

  state = {
    users: [],
  }

  componentDidMount() {
    this.fetchUsers()
  }

  fetchUsers = () => {
    axios.get(`${REACT_APP_USERS_SERVICE_URL}/users`)
      .then(res => this.setState({ users: res.data.data.users }))
      .catch((err) => { console.log(err) })
  }

  filter = (evt) => {
    this.props.userStore.filter = evt.target.value
  }

  createNew = (evt) => {
    if (evt.which === 13) {
      this.props.userStore.createUser(evt.target.value)
      // eslint-disable-next-line
      evt.target.value = ''
    }
  }

  render() {
    const { filteredUsers, filter } = this.props.userStore

    return (
      <div id="users-page">
        <h2>this is user page page</h2>
        <h3>users</h3>
        <input type="text" className="create-new" onKeyPress={this.createNew} />
        <input type="text" className="filter" value={filter} onChange={this.filter} />
        <ul>{
           filteredUsers.map(user => <li className="user" key={user}>{user}</li>)
         }
        </ul>
        <UserList users={this.state.users} />
      </div>
    )
  }
}

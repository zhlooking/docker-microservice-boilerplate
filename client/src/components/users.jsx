/* REACT_APP_USERS_SERVICE_URL */
import React from 'react'
import axios from 'axios'
import PropTypes from 'prop-types'
import { observer, inject } from 'mobx-react'
import UserStore from '../store/user-store'
import UserList from './user_list'
import AddUser from './add_user'
import '../css/users.scss'

@inject('userStore')
@observer
export default class Users extends React.Component {
  static propTypes = {
    userStore: PropTypes.instanceOf(UserStore).isRequired,
  }

  constructor(props) {
    super(props)

    this.state = {
      users: [],
      email: '',
      username: '',
    }

    this.handleAddNewUser = this.handleAddNewUser.bind(this)
    this.handleUserChange = this.handleUserChange.bind(this)
  }

  componentDidMount() {
    this.fetchUsers()
  }

  fetchUsers = () => {
    axios.get(`${REACT_APP_USERS_SERVICE_URL}/users`)
      .then(res => this.setState({ users: res.data.data.users }))
      .catch((err) => { console.log(err) })
  }

  addNewUser = () => {
    const { username, email } = this.state

    axios.post(`${REACT_APP_USERS_SERVICE_URL}/users`, {
      email,
      username,
    })
      .then(() => {
        this.fetchUsers()
        this.setState({ username: '', email: '' })
      })
      .catch(err => { console.log(err) })
  }

  filter = (evt) => {
    this.props.userStore.filter = evt.target.value
  }

  handleUserChange = evt => {
    const { name, value } = evt.target

    this.setState({ [name]: value })
  }

  handleAddNewUser = evt => {
    evt.preventDefault()

    this.addNewUser()
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
        <AddUser
          username={this.state.username}
          email={this.state.email}
          onChange={this.handleUserChange}
          onSubmit={this.handleAddNewUser}
        />
        <UserList users={this.state.users} />
      </div>
    )
  }
}

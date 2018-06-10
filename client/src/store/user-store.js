import { observable, computed } from 'mobx'

class UserStore {
  @observable users = ['Tom', 'Jerry']
  @observable filter = ''

  @computed
  get filteredUsers() {
    const matchesFilter = new RegExp(this.filter, 'i')
    return this.users.filter(user => !this.filter || matchesFilter.test(user))
  }

  createUser(user) {
    this.users.push(user)
  }
}

export default UserStore

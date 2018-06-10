import React from 'react'
import { expect } from 'chai'
import Enzyme, { mount } from 'enzyme'
import Adapter from 'enzyme-adapter-react-16'
import UserStore from '../src/store/user-store'
import UsersPage from '../src/components/users'

Enzyme.configure({ adapter: new Adapter() })
const userStore = new UserStore()

describe('users page rendered succeed', () => {
  it('user list rendered', () => {
    const wrapper = mount(<UsersPage userStore={userStore} />)
    expect(wrapper.find('.user').length).to.equal(2)
  })
})

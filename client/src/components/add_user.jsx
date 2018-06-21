import React from 'react'


export default class extends React.Component {
  render() {
    return (
      <form onSubmit={this.props.handleSubmit}>
        <div className="form-group">
          <input
            name="username"
            className="form-control input-lg"
            type="text"
            placeholder="Enter a username"
            required
            value={this.props.username}
            onChange={this.props.handleChange}
          />
        </div>
        <div className="form-group">
          <input
            name="email"
            className="form-control input-lg"
            type="email"
            placeholder="Enter an email address"
            required
            value={this.props.email}
            onChange={this.props.handleChange}
          />
        </div>
        <input
          type="submit"
          className="btn btn-primary btn-lg btn-block"
          value="Submit"
        />
      </form>
    )
  }
}

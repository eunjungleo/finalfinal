import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import WordsItem from "./WordsItem";
import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

/*
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
*/


class App extends Component {
  state = {
    value: "",
    textList: []
  };

  componentDidMount() {
    this._renderText();
  }
  render() {
    const { textList } = this.state;
    console.log(textList);
    return (
      <div className="App">
        <h1>OneLine App</h1>
        <div>
          <label>
            Text:
            <input
              type="text"
              value={this.state.value}
              onChange={this._handleChange}
            />
          </label>
          <button onClick={this._handleSubmit}>submit</button>
        </div>
        <h2>Long Text</h2>
        {textList.map((text, index) => {
          return (
            <WordsItem
              text={text.text}
              key={index}
              id={text.id}
              handleClick={this._deleteText}
            />
          );
        })}
      </div>
    );
  }
  _handleChange = event => {
    this.setState({ value: event.target.value });
  };
  _handleSubmit = () => {
    const { value } = this.state;
    axios
      .post("/api/wisesaying/", { text: value })
      .then(res => this._renderText());
  };
  _renderText = () => {
    axios
      .get("/api/wisesaying/")
      .then(res => this.setState({ textList: res.data }))
      .catch(err => console.log(err));
  };
  _deleteText = id => {
    axios.delete(`/api/wisesaying/${id}`).then(res => this._renderText());
  };
}

export default App;
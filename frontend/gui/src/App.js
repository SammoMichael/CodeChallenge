import React, { Component } from 'react';
import './App.css';
import 'antd/dist/antd.css'; 

import Article from './components/Article';
import CustomLayout from './containers/Layout';
import ArticleListView from './containers/ArticleListView';

class App extends Component {
  render() {
    return (
      <div className="App">
          <CustomLayout>
            <ArticleListView/>
          </CustomLayout>
      </div>
    );
  }
}

export default App;

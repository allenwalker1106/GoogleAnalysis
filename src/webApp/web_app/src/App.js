
import React from 'react';
import SearchBar from './components/search_bar';
import NavSection from './components/nav_section'
import ThreadInfo from './components/thread_info'
import Chart from './components/chart'
class App extends React.Component {
  constructor(props){
    super(props)
    this.state={
      tags:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      keywords_props:{},
      response: {},
      document:[]
    }
  }

  setPredictTag(childData){
    this.setState({
      response:childData
    })
    var predict_array = this.state.response.tags
    var keywords_props =  this.state.response.keywords_props
    this.setState({
      tags:predict_array,
      keywords_props:keywords_props
    })
  }

  setSearchByTagResult(childData){
    this.setState({
      document:childData.response
    })
  }

  setSearchByKeywordResult(childData){
    this.setState({
      document:childData.response
    })
    // console.log(this.state.document)
    // console.log('setSearchByKeywordResult')
    // console.log(this.state.document)
  }

  render(){
    return(
      <div style={{display: 'flex'}}>
        <div  style={{flex: 0}}>
          <NavSection></NavSection>
        </div>
        <div style={{flex:1}}>
          <div>
            <SearchBar setSearchByTagResult={this.setSearchByTagResult.bind(this)} setPredictTag={this.setPredictTag.bind(this)} setSearchByKeywordResult={this.setSearchByKeywordResult.bind(this)}></SearchBar>
          </div>
          <div>
            <Chart documents={this.state.document}></Chart>
          </div>
        </div>
        
        <div>
          <ThreadInfo tags ={this.state.tags} keywords_props={this.state.keywords_props}></ThreadInfo>
        </div>
      </div>
    );
  }
}


export default App;

import React from 'react'
import '../static/styles/Home.css'

import SearchBar from '../components/search_bar';
import TagDisplay from '../components/tag_display';
import KeywordDisplay from '../components/keyword_display'
import ThreadDisplay from '../components/thread_info'
import Chart from '../components/chart'


export default class Home extends React.Component{
    constructor(props){
        super(props)
        this.state={
          tags:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          keywords_props:{},
          response: {},
          document:[]
        }
      }

      sortKeyword(arr_keyword){
        var items = Object.keys(arr_keyword).map(function(key) {
          return [key, arr_keyword[key]];
        });
        
        // Sort the array based on the second element
        items.sort(function(first, second) {
          return second[1] - first[1];
        });
        var top10=items.slice(0,10)
        var dict_keyword = {}
        for(var index in top10){
          let key = top10[index][0]
          let val = top10[index][1]
          dict_keyword[key]=val
        }
        
        return dict_keyword
      }
      
    
      setPredictTag(childData){
        this.setState({
            tags:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            keywords_props:{},
            response: {},
            document:[]
          })
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
            tags:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            keywords_props:{},
            response: {},
            document:[]
          })
        this.setState({
          document:childData.response
        })

        
        var arr_keyword= []
        for ( var index in childData.response){
          arr_keyword=Object.assign({},arr_keyword,childData.response[index].keywords_props)
        }
        
        this.setState({
          keywords_props:this.sortKeyword(arr_keyword)
        })
      }
    
      setSearchByKeywordResult(childData){
        this.setState({
            tags:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            keywords_props:{},
            response: {},
            document:[]
          })
        this.setState({
          document:childData.response
        })

        var arr_keyword= []
        for ( var index in childData.response){
          arr_keyword=Object.assign({},arr_keyword,childData.response[index].keywords_props)
        }
        
        this.setState({
          keywords_props:this.sortKeyword(arr_keyword)
        })

      }
    render(){
        return (

            <div id="container">
              <a id="button" className="show" href='#container'>Top</a>
              <div id="sideMenu">
                <h1>Google Analysis</h1>
                <ul className="menu">
                  <li>Main</li>
                  <li><a href="#chart_statistic">Chart</a></li>
                  <li><a href='#thread_data'>Data</a> </li>
                </ul>
              </div>
              <div id="content">
                <div id="titleBar">
                    <div id="profilePic">
                        <img src="https://i.stack.imgur.com/34AD2.jpg" alt='icon'/>
                    </div>
                    <span className="controls activeControl">Login</span>
                    <span className="controls">Signup</span>
                    <SearchBar  setSearchByTagResult={this.setSearchByTagResult.bind(this)} setPredictTag={this.setPredictTag.bind(this)} setSearchByKeywordResult={this.setSearchByKeywordResult.bind(this)}></SearchBar>
                </div>
                <div className="mainChart">
                  {/* <canvas id="chart" /> */}
                  <h2 id="thread_data">Google group info</h2>
                  <div className="clearFix" />
                  <div>
                    <ThreadDisplay dict_data={this.state.response.dict_data}></ThreadDisplay>
                    <TagDisplay tags ={this.state.tags}></TagDisplay>
                  </div>
                  

                  <KeywordDisplay keywords_props={this.state.keywords_props}></KeywordDisplay>
                  
                  <h2 id="chart_statistic">Chart Statistics</h2>
                  <Chart data={this.state.document} ></Chart>
                </div>
              </div>
            </div>
          );
    }
}
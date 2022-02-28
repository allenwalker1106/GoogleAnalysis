import React from 'react';
import { Bar } from 'react-chartjs-2';
import ThreadCodeDisplay from './filter_sumary'

class Chart extends React.Component{
    constructor(props){
        super(props)
        this.state={
            tag_list:['Reading from folder','Automatic model selection','Substitution model options','Bug report','Rate heterogeneity options','Ascertainment bias correction option','Partition model options','Mixture model options','Heterotachy model options','Site specific frequency model options','Polymorphism aware model options','Automatic partition merging','Tree search parameters','Constrained tree search','Ultrafast bootstrap parameters','Nonparametric bootstrap','Single branch tests','Tree topology tests','Concordance factor','Phylogenetic dating','Ancestral sequence reconstruction','Constructing consensus tree','Propose feature','Likelihood mapping analysis','Utilizing multi core CPUs','Inferring site specific rates','Reducing impact of severe model violations with UFBoot'],
            
        }
    }

    processData(){
        if(this.props.data){
            var data=this.props.data
            var arr_data = []
            for(var i=0;i<this.state.tag_list.length;i++)
                arr_data.push(0)
            for(var i in data)
            {
                var tags = data[i]['tags']
                
                for(var i=0;i<tags.length;i++)
                    arr_data[i]+=tags[i]
            }
    
            return arr_data
        }
        return []
    }


    getThreadCodeList(){
        if(this.props.data){
            var data=this.props.data
            var arr_threadCode = []

            for(var i in data)
            {
                arr_threadCode.push(data[i]['thread_code'])
            }
    
            return arr_threadCode
        }
        return []
    }

    getLastUpdateList(){
        if(this.props.data){
            var data=this.props.data
            var arr_threadCode = []

            for(var i in data)
            {
                arr_threadCode.push(data[i]['last_update'])
            }
    
            return arr_threadCode
        }
        return []
    }

    getInitDateList(){
        if(this.props.data){
            var data=this.props.data
            var arr_threadCode = []

            for(var i in data)
            {
                arr_threadCode.push(data[i]['init_date'])
            }
    
            return arr_threadCode
        }
        return []
    }


    createDateSet(){
        const dataset = {
            
              labels: this.state.tag_list,
              datasets:[
                  {
                        label:'Tag Distribution Diagram',
                        
                        data:this.processData(),
                        backgroundColor: [
                                    'rgba(255, 99, 132, 0.2)',
                                    'rgba(54, 162, 235, 0.2)',
                                    'rgba(255, 206, 86, 0.2)',
                                    'rgba(75, 192, 192, 0.2)',
                                    'rgba(153, 102, 255, 0.2)',
                                    'rgba(255, 159, 64, 0.2)',
                                    'rgba(255, 99, 132, 0.2)',
                                    'rgba(54, 162, 235, 0.2)',
                                    'rgba(255, 206, 86, 0.2)',
                                    'rgba(75, 192, 192, 0.2)',
                                    'rgba(153, 102, 255, 0.2)',
                                    'rgba(255, 159, 64, 0.2)',
                                    'rgba(255, 99, 132, 0.2)',
                                    'rgba(54, 162, 235, 0.2)',
                                    'rgba(255, 206, 86, 0.2)',
                                    'rgba(75, 192, 192, 0.2)',
                                    'rgba(153, 102, 255, 0.2)',
                                    'rgba(255, 159, 64, 0.2)',
                                    'rgba(255, 99, 132, 0.2)',
                                    'rgba(54, 162, 235, 0.2)',
                                    'rgba(255, 206, 86, 0.2)',
                                    'rgba(75, 192, 192, 0.2)',
                                    'rgba(153, 102, 255, 0.2)',
                                    'rgba(255, 159, 64, 0.2)',
                                    'rgba(75, 192, 192, 0.2)',
                                    'rgba(153, 102, 255, 0.2)',
                                    'rgba(255, 159, 64, 0.2)',
                        ],
                        borderColor: [
                                    'rgba(255, 99, 132, 1)',
                                    'rgba(54, 162, 235, 1)',
                                    'rgba(255, 206, 86, 1)',
                                    'rgba(75, 192, 192, 1)',
                                    'rgba(153, 102, 255, 1)',
                                    'rgba(255, 159, 64, 1)',
                                    'rgba(255, 99, 132, 1)',
                                    'rgba(54, 162, 235, 1)',
                                    'rgba(255, 206, 86, 1)',
                                    'rgba(75, 192, 192, 1)',
                                    'rgba(153, 102, 255, 1)',
                                    'rgba(255, 159, 64, 1)',
                                    'rgba(255, 99, 132, 1)',
                                    'rgba(54, 162, 235, 1)',
                                    'rgba(255, 206, 86, 1)',
                                    'rgba(75, 192, 192, 1)',
                                    'rgba(153, 102, 255, 1)',
                                    'rgba(255, 159, 64, 1)',
                                    'rgba(255, 99, 132, 1)',
                                    'rgba(54, 162, 235, 1)',
                                    'rgba(255, 206, 86, 1)',
                                    'rgba(75, 192, 192, 1)',
                                    'rgba(153, 102, 255, 1)',
                                    'rgba(255, 159, 64, 1)',
                                    'rgba(75, 192, 192, 1)',
                                    'rgba(153, 102, 255, 1)',
                                    'rgba(255, 159, 64, 1)',
                                  ],
                              borderWidth: 2
                    }
              ]
            };
        return dataset
    }

    render(){
        var dataset=this.createDateSet()
        // this.processData()
        var arr_threadCode =this.getThreadCodeList()
        var arr_initDate=  this.getInitDateList()
        var arr_lastUpdate = this.getLastUpdateList()
        const options = {
        scales: {
            yAxes: [
            {
                ticks: {
                beginAtZero: true,
                },
            },
            ],
        },
        };
        return(
            <div>
                <Bar data={dataset} options={options} />
                <ThreadCodeDisplay thread_code={arr_threadCode} init_date={arr_initDate} last_update={arr_lastUpdate}></ThreadCodeDisplay>
            </div>   
        )
    }
}


export default Chart;
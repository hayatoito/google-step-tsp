import { PolymerElement, html } from '@polymer/polymer/polymer-element.js';

class MyTsp extends PolymerElement {
  static get template() {
    return html`
    <style>
      #graph {
        width: 100%;
      }
    </style>
    <svg id="graph"></svg>
`;
  }

  static get properties() {
    return {
      inputfile: {
        type: String
      },
      outputfile: {
        type: String
      },
      pathlength: {
        type: Number,
        notify: true
      }
    };
  }

  // Workaround: See https://stackoverflow.com/questions/13053096/avoid-data-caching-when-using-d3-text
  unique(url) {
    return url + '?' + Math.floor(Math.random() * 1000000);
  }

  draw() {
    if (!this.inputfile || !this.outputfile) {
      return;
    }
    const width = this.$.graph.getBoundingClientRect().width;
    const height = Math.round((width * 900) / 1600);

    const graph = d3.select(this.$.graph);
    graph.selectAll('*').remove();
    graph.attr('height', height);

    const x = d3.scaleLinear().range([4, width - 4]);
    const y = d3.scaleLinear().range([4, height - 4]);

    Promise.all([
      d3
        .csv(this.inputfile)
        .then(cities =>
          cities.map(city => ({ x: parseFloat(city.x), y: parseFloat(city.y) }))
        ),
      d3
        .csv(this.unique(this.outputfile))
        .then(tour => tour.map(v => parseInt(v.index)))
    ])
      .then(results => {
        const [cities, tour] = results;
        this.pathlength = caluculateDistance(cities, tour);
        drawGraph(cities, tour);
      })
      .catch(e => console.error(e));

    function caluculateDistance(cities, tour) {
      function distance(i, j) {
        return Math.sqrt(
          Math.pow(cities[i].x - cities[j].x, 2) +
            Math.pow(cities[i].y - cities[j].y, 2)
        );
      }
      const N = cities.length;
      let pathlength = 0;
      for (let i = 0; i < N; ++i) {
        pathlength += distance(tour[i], tour[(i + 1) % N]);
      }
      return Math.round(pathlength * 100) / 100;
    }

    function drawGraph(cities, tour) {
      x.domain([0, d3.max(cities, d => d.x)]);
      y.domain([0, d3.max(cities, d => d.y)]);

      graph
        .selectAll('g')
        .data(cities)
        .enter()
        .append('circle')
        .attr('class', 'dot')
        .attr('r', 5)
        .attr('cx', d => x(d.x))
        .attr('cy', d => y(d.y))
        .attr('stroke-width', '0.5px')
        .attr('stroke', '#fff')
        .style('fill', '#4285f4');

      const lineFunction = d3
        .line()
        .x(d => x(cities[d].x))
        .y(d => y(cities[d].y))
        .curve(d3.curveLinear);

      const path = graph
        .append('path')
        .attr('d', lineFunction(tour.concat(tour[0])))
        .attr('stroke', '#666')
        .attr('stroke-width', 3)
        .attr('opacity', 0.6)
        .attr('fill', 'none');

      const totalLength = path.node().getTotalLength();

      path
        .attr('stroke-dasharray', totalLength + ' ' + totalLength)
        .attr('stroke-dashoffset', totalLength)
        .transition()
        .duration(totalLength)
        .ease(d3.easeLinear)
        .attr('stroke-dashoffset', 0);
    }
  }
}

customElements.define('my-tsp', MyTsp);

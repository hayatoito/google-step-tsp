import "./node_modules/@polymer/polymer/polymer-legacy.js";
import "./node_modules/@polymer/iron-flex-layout/iron-flex-layout.js";
import "./node_modules/@polymer/iron-icons/iron-icons.js";
import "./node_modules/@polymer/iron-icons/maps-icons.js";
import "./node_modules/@polymer/paper-fab/paper-fab.js";
import "./node_modules/@polymer/paper-radio-button/paper-radio-button.js";
import "./node_modules/@polymer/paper-radio-group/paper-radio-group.js";
import "./travelling-salesman-problem.js";
import {
  PolymerElement,
  html
} from "./node_modules/@polymer/polymer/polymer-element.js";
class TravellingSalesmanProblemVisualizer extends PolymerElement {
  static get template() {
    return html`
    <style>
      :host {
        @apply --layout-horizontal;
      }
      [nav] {
        width: 220px;
        @apply --layout-vertical;
      }
      travelling-salesman-problem {
        width: 100%;
        margin-top: 16px;
      }
      #control {
        padding: 8px;
        @apply --layout-vertical;
      }
      #result {
        margin-top: 8px;
      }
      #challenges {
        @apply --layout-flex;
        @apply --layout-vertical;
      }
      #solvers {
        @apply --layout-flex;
        @apply --layout-vertical;
      }
      paper-radio-button {
        display: block;
      }
    </style>
    <div nav="">
      <div>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/272px-Google_2015_logo.svg.png" height="50">
        <h4>Travelling Salesman Problem Challenges</h4>
      </div>
      <div id="control">
        <paper-fab icon="maps:directions-run" on-click="run"></paper-fab>
        <div id="result"><span>{{result}}</span> m</div>
      </div>
      <div>
        <h4>Challenges</h4>
        <paper-radio-group id="challenges" selected="0">
          <paper-radio-button name="0">0: N=5</paper-radio-button>
          <paper-radio-button name="1">1: N=8</paper-radio-button>
          <paper-radio-button name="2">2: N=16</paper-radio-button>
          <paper-radio-button name="3">3: N=64</paper-radio-button>
          <paper-radio-button name="4">4: N=128</paper-radio-button>
          <paper-radio-button name="5">5: N=512</paper-radio-button>
          <paper-radio-button name="6">6: N=2048</paper-radio-button>
        </paper-radio-group>
      </div>
      <div>
        <h4>Solvers</h4>
        <paper-radio-group id="solvers" selected="/output">
          <paper-radio-button name="/output">Your output</paper-radio-button>
          <paper-radio-button name="/sample/random">sample/random</paper-radio-button>
          <paper-radio-button name="/sample/greedy">sample/greedy</paper-radio-button>
          <paper-radio-button name="/sample/sa">sample/sa</paper-radio-button>
        </paper-radio-group>
      </div>
      <div>
        <h4>Links</h4>
        <div><a href="https://github.com/hayatoito/google-step-tsp/blob/gh-pages/README.md">README</a></div>
      </div>
    </div>
    <travelling-salesman-problem id="tsp" pathlength="{{result}}"></travelling-salesman-problem>
`;
  }

  static get is() {
    return "travelling-salesman-problem-visualizer";
  }
  ready() {
    super.ready();
    console.log(this);
    var self = this;
    this.$.challenges.addEventListener("paper-radio-group-changed", e => {
      self.draw();
    });
    this.$.solvers.addEventListener("paper-radio-group-changed", () => {
      self.draw();
    });
    self.draw();
  }
  run() {
    this.$.tsp.draw();
  }
  draw() {
    this.$.tsp.inputfile = "/input_" + this.$.challenges.selected + ".csv";
    this.$.tsp.solutionfile =
      this.$.solvers.selected + "_" + this.$.challenges.selected + ".csv";
    this.$.tsp.draw();
  }
}

customElements.define(
  TravellingSalesmanProblemVisualizer.is,
  TravellingSalesmanProblemVisualizer
);

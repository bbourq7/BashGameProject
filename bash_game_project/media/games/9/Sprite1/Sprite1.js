/* eslint-disable require-yield, eqeqeq */

import {
  Sprite,
  Trigger,
  Watcher,
  Costume,
  Color,
  Sound,
} from "https://unpkg.com/leopard@^1/dist/index.esm.js";

export default class Sprite1 extends Sprite {
  constructor(...args) {
    super(...args);

    this.costumes = [
      new Costume("costume2", "./Sprite1/costumes/costume2.svg", {
        x: 21.696679145637177,
        y: 48.49500255693951,
      }),
      new Costume("costume1", "./Sprite1/costumes/costume1.svg", {
        x: 21.69667988411706,
        y: 43.5571280326144,
      }),
      new Costume("costume3", "./Sprite1/costumes/costume3.svg", {
        x: 21.696674884117073,
        y: 48.49501026622687,
      }),
      new Costume("costume4", "./Sprite1/costumes/costume4.svg", {
        x: 21.696674884117073,
        y: 46.75205648972337,
      }),
      new Costume("costume5", "./Sprite1/costumes/costume5.svg", {
        x: 16.714386871177226,
        y: 35.117566634430915,
      }),
      new Costume("costume6", "./Sprite1/costumes/costume6.svg", {
        x: 16.71438926220378,
        y: 35.11756846463874,
      }),
    ];

    this.sounds = [new Sound("Meow", "./Sprite1/sounds/Meow.wav")];

    this.triggers = [
      new Trigger(
        Trigger.KEY_PRESSED,
        { key: "left arrow" },
        this.whenKeyLeftArrowPressed
      ),
      new Trigger(
        Trigger.KEY_PRESSED,
        { key: "right arrow" },
        this.whenKeyRightArrowPressed
      ),
      new Trigger(
        Trigger.KEY_PRESSED,
        { key: "up arrow" },
        this.whenKeyUpArrowPressed
      ),
      new Trigger(
        Trigger.KEY_PRESSED,
        { key: "down arrow" },
        this.whenKeyDownArrowPressed
      ),
      new Trigger(
        Trigger.BROADCAST,
        { name: "message1" },
        this.whenIReceiveMessage1
      ),
      new Trigger(
        Trigger.BROADCAST,
        { name: "message 2" },
        this.whenIReceiveMessage2
      ),
    ];
  }

  *whenKeyLeftArrowPressed() {
    this.costume = "costume5";
    this.x -= 10;
    this.ifOnEdgeBounce();
  }

  *whenKeyRightArrowPressed() {
    this.costume = "costume6";
    this.x += 10;
    this.ifOnEdgeBounce();
  }

  *whenKeyUpArrowPressed() {
    this.costume = "costume3";
    this.broadcast("message 2");
    this.y += 10;
    this.ifOnEdgeBounce();
    this.direction = 90;
  }

  *whenKeyDownArrowPressed() {
    this.costume = "costume1";
    this.broadcast("message1");
    this.y -= 10;
    this.ifOnEdgeBounce();
    this.direction = 90;
  }

  *whenIReceiveMessage1() {
    if (this.keyPressed("up arrow")) {
      yield* this.wait(0.2);
      this.costume = "costume2";
      yield* this.wait(0.2);
      this.costume = "costume1";
    }
  }

  *whenIReceiveMessage2() {
    if (this.keyPressed("down arrow")) {
      yield* this.wait(0.2);
      this.costume = "costume3";
      yield* this.wait(0.2);
      this.costume = "costume4";
    }
  }
}

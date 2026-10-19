(function () {
  "use strict";

  var records = [];
  var scheme = null;
  var applyingTheme = false;
  var pendingTheme = false;

  function currentScheme() {
    return document.body.getAttribute("data-md-color-scheme") === "slate"
      ? "dark"
      : "light";
  }

  function playerOptions(theme, poster) {
    var options = {
      fit: "width",
      theme: "calpdf-" + theme,
      autoPlay: false,
      preload: true,
      idleTimeLimit: 2.5,
      terminalLineHeight: 1.2,
    };

    var codeFont = getComputedStyle(document.body)
      .getPropertyValue("--md-code-font-family")
      .trim();

    if (codeFont) {
      options.terminalFontFamily = codeFont;
    }

    if (poster) {
      options.poster = poster;
    }

    return options;
  }

  function createEntry(record, theme, hidden) {
    var stage = document.createElement("div");
    stage.className = "asciinema-stage";
    if (hidden) {
      stage.setAttribute("aria-hidden", "true");
    }
    record.el.appendChild(stage);

    var entry = {
      stage: stage,
      player: null,
      playing: false,
      started: false,
    };

    entry.player = window.AsciinemaPlayer.create(
      record.cast,
      stage,
      playerOptions(theme, record.poster),
    );

    function markPlaying() {
      entry.playing = true;
      entry.started = true;
    }

    entry.player.addEventListener("play", markPlaying);
    entry.player.addEventListener("pause", function () {
      entry.playing = false;
    });
    entry.player.addEventListener("ended", function () {
      entry.playing = false;
    });

    return entry;
  }

  function createRecord(el) {
    var cast = el.getAttribute("data-asciinema-cast");
    if (!cast) {
      return null;
    }

    var record = {
      el: el,
      cast: cast,
      poster: el.getAttribute("data-asciinema-poster"),
      entries: {},
      active: null,
    };

    var activeTheme = scheme;
    var inactiveTheme = activeTheme === "light" ? "dark" : "light";

    record.entries[activeTheme] = createEntry(record, activeTheme, false);
    record.entries[inactiveTheme] = createEntry(record, inactiveTheme, true);
    record.active = record.entries[activeTheme];

    return record;
  }

  function activate(record, theme, done) {
    var source = record.active;
    var target = record.entries[theme];

    if (!target || source === target) {
      done();
      return;
    }

    var time = 0;
    try {
      time = Number(source.player.getCurrentTime()) || 0;
    } catch (error) {
      time = 0;
    }

    var duration = null;
    try {
      duration = source.player.getDuration();
    } catch (error) {
      duration = null;
    }

    var playing = source.playing;
    var ended =
      !playing && typeof duration === "number" && time >= duration - 0.001;
    var started = source.started;
    var finished = false;

    function finish() {
      if (finished) {
        return;
      }
      finished = true;

      source.stage.setAttribute("aria-hidden", "true");
      target.stage.removeAttribute("aria-hidden");
      record.active = target;

      if (playing) {
        try {
          source.player.pause();
        } catch (error) {
          // The source is hidden now, so a failed pause cannot affect the page.
        }
      }

      done();
    }

    function fail() {
      if (finished) {
        return;
      }
      finished = true;

      try {
        target.player.pause();
      } catch (error) {
        // The target stays hidden if it cannot be paused.
      }

      if (playing) {
        source.player.play().catch(function () {
          // If playback cannot resume, leave the source paused rather than
          // swapping to a player that was never positioned.
        });
      }

      done();
    }

    // Before the first play, both players are still on the poster. Swapping
    // them keeps the initial frame and the start overlay intact.
    if (!started) {
      finish();
      return;
    }

    if (ended) {
      // Play once to dismiss the start overlay, then seek to the end to
      // restore the ended state.
      target.player
        .play()
        .then(function () {
          return target.player.seek(time);
        })
        .then(finish)
        .catch(fail);
      return;
    }

    var positioned = target.player.seek(time);

    if (playing) {
      positioned
        .then(function () {
          return target.player.play();
        })
        .then(finish)
        .catch(fail);
    } else {
      positioned
        .then(function () {
          // Seeking leaves the start overlay up. A hidden play/pause
          // returns the other player to the normal paused state.
          return target.player.play().then(function () {
            return target.player.pause();
          });
        })
        .then(finish)
        .catch(fail);
    }
  }

  function refresh() {
    var next = currentScheme();

    if (next === scheme) {
      return;
    }

    if (applyingTheme) {
      pendingTheme = true;
      return;
    }

    scheme = next;
    applyingTheme = true;

    var remaining = records.length;

    function finishOne() {
      remaining -= 1;
      if (remaining > 0) {
        return;
      }

      applyingTheme = false;
      if (pendingTheme) {
        pendingTheme = false;
        refresh();
      }
    }

    records.forEach(function (record) {
      activate(record, next, finishOne);
    });
  }

  function init() {
    if (!window.AsciinemaPlayer) {
      return;
    }

    scheme = currentScheme();
    document.querySelectorAll("[data-asciinema-cast]").forEach(function (el) {
      var record = createRecord(el);
      if (record) {
        records.push(record);
      }
    });

    if (records.length === 0) {
      return;
    }

    var themeObserver = new MutationObserver(refresh);
    themeObserver.observe(document.body, {
      attributes: true,
      attributeFilter: ["data-md-color-scheme"],
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

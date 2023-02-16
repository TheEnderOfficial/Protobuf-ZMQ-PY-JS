import protobufjs from "protobufjs"
import {Reply} from "zeromq";

async function main() {
    const sock = new Reply();
    const root = await protobufjs.load("../common/communication.proto");

    await sock.bind("tcp://127.0.0.1:3000");
    console.log("Server/Producer bound to port 3000");

    for await (const [msg] of sock) {
        const AwesomeMessage = root.lookupType("awesomepackage.AwesomeMessage")

        try {
            const d = AwesomeMessage.decode(msg);
            const x = d.toJSON();
            console.log(x.awesomeField);

            const n = {
                awesomeField: `I recieve ${x.awesomeField}`
            }
            const e = AwesomeMessage.verify(n);
            if (e) throw Error(e);
            const m = AwesomeMessage.encode(n).finish();
            await sock.send(m)
        }
        catch (e) {
            console.error(e);
        }
    }

}

main();
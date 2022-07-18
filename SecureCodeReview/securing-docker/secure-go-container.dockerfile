FROM golang:1.15 as build

COPY . .

ENV GOPATH=""
ENV CGO_ENABLED=0
ENV GOOS=linux
ENV GOARCH=amd64
RUN go build -trimpath -v -a -o myapp -ldflags="-w -s"
RUN chmod +x go-goof

RUN useradd -u 12345 moby

FROM scratch
COPY --from=build /go/myapp /myapp
COPY --from=build /etc/passwd /etc/passwd
USER moby

ENTRYPOINT ["/myapp"]

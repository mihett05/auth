import { Injectable } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { UsersService } from '../users/users.service';
import { User } from '../users/entities/user.entity';

@Injectable()
export class AuthService {
  constructor(
    private readonly _usersService: UsersService,
    private readonly _jwtService: JwtService
  ) {}

  async validate(login: string, password: string): Promise<User | undefined> {
    return await this._usersService.findByAuth(login, password);
  }

  async login(user: any) {
    const payload = {
      username: user.username
    };
    return {
      access_token: this._jwtService.sign(payload)
    };
  }
}
